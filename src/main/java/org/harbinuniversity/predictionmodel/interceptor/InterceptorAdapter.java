/** created by leihong.pan at 2017/1/22 15:57 */
package org.harbinuniversity.predictionmodel.interceptor;

import org.springframework.boot.autoconfigure.web.WebMvcAutoConfiguration;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurerAdapter;

/**
 *
 *
 * @author leihong.pan
 */
@Configuration
public class InterceptorAdapter extends WebMvcConfigurerAdapter {

    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(new LoginVaildInterceptor()).addPathPatterns("/rest/**").excludePathPatterns("/system/**");
        super.addInterceptors(registry);
    }
}
