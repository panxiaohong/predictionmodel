/** created by leihong.pan at 2017/1/20 10:27 */
package org.harbinuniversity.predictionmodel.util;

import lombok.extern.slf4j.Slf4j;
import org.python.core.*;
import org.python.util.PythonInterpreter;
import org.springframework.stereotype.Component;

import java.net.URL;
import java.util.*;

/**
 * init pythonInterpreter with Factory pattern
 *
 * @author leihong.pan
 */
@Slf4j
@Component
public class PythonFactory {

    static {
        Properties props = new Properties();
        props.setProperty("python.home", PropertiesUtils.getProperty("python.home"));
        props.setProperty("python.security.respectJavaAccessibility", PropertiesUtils.getProperty("python.security.respectJavaAccessibility"));
        props.setProperty("python.console.encoding", PropertiesUtils.getProperty("python.console.encoding"));
        props.setProperty("python.import.site", PropertiesUtils.getProperty("python.import.site"));
        PythonInterpreter.initialize(System.getProperties(), props, null);
    }

    private PythonFactory() {
    }

    /** get the pythonInterpreter */
    public static PythonInterpreter getPythonInterpreter() {
        return new PythonInterpreter();
    }

    /** get a pyfunction to execute python function */
    public static PyFunction getPyFunction(URL pyFileUrl, String function) {
        if(Objects.nonNull(pyFileUrl)) {
            PythonInterpreter interpreter = getPythonInterpreter();
            interpreter.execfile(pyFileUrl.getPath());
            return interpreter.get(function, PyFunction.class);
        }
        return null;
    }

    /**
     * @param pyFileUrl     python programming file
     * @param function      that you will be called to solve the business;
     * @param params        The parameters of the  @function
     */
    public static PyObject getResult(URL pyFileUrl, String function, Map<String, Object> params) {
        if(Objects.nonNull(pyFileUrl)) {
            PythonInterpreter interpreter = new PythonInterpreter();
            interpreter.exec("import sys");
            log.info(PythonFactory.class.getResource("/").getPath().substring(1).replace("/","\\"));
            interpreter.exec("sys.path.append('"+PythonFactory.class.getResource("/").getPath().substring(1)+"')");
            interpreter.execfile(pyFileUrl.getPath());
            PyFunction pyFunction = null;
            Map<PyObject, PyObject> table = new HashMap<PyObject, PyObject>();
            pyFunction = interpreter.get(function, PyFunction.class);
            //不使用java8的新的api,Iterator的方式其更高效
            Iterator<String> iterator = params.keySet().iterator();
            String key;
            while(iterator.hasNext()){
                key=iterator.next();
                table.put(new PyString(key),PyJavaType.wrapJavaObject(params.get(key)));
            }
            PyDictionary dict = new PyDictionary(table);
            PyObject result = pyFunction.__call__(dict);
            return result;
        }
        return null;
    }

}
