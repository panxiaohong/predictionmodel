/** created by leihong.pan at 2017/1/20 10:27 */

import lombok.extern.slf4j.Slf4j;
import org.python.core.PyFunction;
import org.python.util.PythonInterpreter;
import org.springframework.util.ResourceUtils;

import java.io.FileNotFoundException;
import java.net.URL;
import java.util.Properties;

/**
 * init pythonInterpreter with Factory pattern
 *
 * @author leihong.pan
 */
@Slf4j
public class PythonFactory {

    static {
        Properties props = new Properties();
        props.setProperty("python.home",PropertiesUtils.getProperty("python.home"));
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
        try{
            if(ResourceUtils.getFile(pyFileUrl.getFile()).exists()) {
                PythonInterpreter interpreter = getPythonInterpreter();
                interpreter.execfile(pyFileUrl.toString());
                return interpreter.get(function, PyFunction.class);
            } else {
                log.info("文件[{}]不存在", pyFileUrl);
            }
        } catch(FileNotFoundException e) {
            log.error("读取文件[{}]出错", pyFileUrl);
        }
        return null;
    }

}
