/** created by leihong.pan at 2017/1/20 13:50 */
package org.harbinuniversity.predictionmodel.util;

import org.springframework.core.env.Environment;

/**
 * @author leihong.pan
 */
public class PropertiesUtils {

    private static Environment environment = ApplicationContextHolder.getInstence(Environment.class);

    public static String getProperty(String key, String defaultValue) {
        return environment.getProperty(key) == null ? defaultValue : environment.getProperty(key);
    }

    public static String getProperty(String key) {
        return getProperty(key, null);
    }
}