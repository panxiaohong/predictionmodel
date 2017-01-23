/** created by leihong.pan at 2017/1/22 16:29 */
package org.harbinuniversity.predictionmodel.Fliter;

import lombok.extern.slf4j.Slf4j;
import org.harbinuniversity.predictionmodel.util.HttpServletContext;

import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

/**
 * @author leihong.pan
 */
@WebFilter
@Slf4j
public class HttpBindFilter implements Filter {
    @Override
    public void init(FilterConfig filterConfig) throws ServletException {}

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
        HttpServletContext.setContext((HttpServletRequest) request, (HttpServletResponse) response);
        chain.doFilter(request, response);
        HttpServletContext.removeContext();
    }

    @Override
    public void destroy() {}
}
