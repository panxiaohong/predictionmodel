/** created by leihong.pan at 2017/1/22 16:47 */
package org.harbinuniversity.predictionmodel.util;

import lombok.AllArgsConstructor;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 *
 *
 * @author leihong.pan
 */
public class HttpServletContext {

    @AllArgsConstructor
    private static class Context {
        private final HttpServletRequest httpServletRequest;
        private final HttpServletResponse httpServletResponse;
    }
    private static ThreadLocal<Context> contextThreadLocal = new ThreadLocal();

    public static void setContext(HttpServletRequest request,HttpServletResponse response){
        contextThreadLocal.set(new Context(request,response));
    }

    public static HttpServletRequest getRequest(){
        return contextThreadLocal.get().httpServletRequest;
    };
    public static HttpServletResponse getResponse(){
        return contextThreadLocal.get().httpServletResponse;
    };
    public static void removeContext() {
        contextThreadLocal.remove();
    }






}
