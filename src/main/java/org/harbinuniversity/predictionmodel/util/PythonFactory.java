/** created by leihong.pan at 2017/1/20 10:27 */
package org.harbinuniversity.predictionmodel.util;

import lombok.extern.slf4j.Slf4j;
import org.python.core.PyFunction;
import org.python.util.PythonInterpreter;
import org.springframework.stereotype.Component;
import org.springframework.util.ResourceUtils;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.URL;
import java.util.Objects;
import java.util.Properties;

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
        props.setProperty("python.console.encoding",PropertiesUtils.getProperty("python.console.encoding"));
        props.setProperty("python.import.site",PropertiesUtils.getProperty("python.import.site"));
        PythonInterpreter.initialize(props, System.getProperties(),null);
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

}
