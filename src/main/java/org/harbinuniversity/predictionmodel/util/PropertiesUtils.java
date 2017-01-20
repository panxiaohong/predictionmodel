/** created by leihong.pan at 2017/1/20 13:50 */
package org.harbinuniversity.predictionmodel.util;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.env.Environment;

/**
 *
 *
 * @author leihong.pan
 */
public class PropertiesUtils {
    //private static Environment environment = ApplicationContextHolder.getInstence(Environment.class);
    @Autowired
    private static Environment env;
    public static String  getProperty(String key){
        return env.getProperty(key);
    };
}