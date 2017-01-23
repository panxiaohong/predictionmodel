/** created by leihong.pan at 2017/1/22 15:45 */
package org.harbinuniversity.predictionmodel.interceptor;

import lombok.extern.slf4j.Slf4j;
import org.springframework.web.servlet.handler.HandlerInterceptorAdapter;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 *
 *
 * @author leihong.pan
 */
@Slf4j
public class LoginVaildInterceptor extends HandlerInterceptorAdapter {


    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        log.info(request.getRemoteHost());
        return super.preHandle(request, response, handler);
    }
}
