/** created by leihong.pan at 2017/1/20 14:00 */
package org.harbinuniversity.predictionmodel.util;

import com.google.common.collect.Maps;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.BeansException;
import org.springframework.beans.factory.config.BeanFactoryPostProcessor;
import org.springframework.beans.factory.config.ConfigurableListableBeanFactory;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationContextAware;

import java.util.Arrays;
import java.util.Map;

/**
 * @author leihong.pan
 */
@Slf4j
public class ApplicationContextHolder implements ApplicationContextAware, BeanFactoryPostProcessor {

    private static ApplicationContext applicationContext = null;
    //缓存bean
    private static Map<Class<?>, String> nameMap = Maps.newHashMap();

    @Override
    public void setApplicationContext(ApplicationContext applicationContext) throws BeansException {
        this.applicationContext = applicationContext;
    }

    @Override
    public void postProcessBeanFactory(ConfigurableListableBeanFactory configurableListableBeanFactory) throws BeansException {
        //todo
    }

    /** 获取spring中的相应的bean*/
    static <T> T getInstence(Class<T> tClass) {
        String beanName = nameMap.get(tClass);
        if(beanName == null) {
            String[] beanNames = applicationContext.getBeanNamesForType(tClass);
            if(beanNames.length == 0)
                throw new RuntimeException("类:" + tClass + "没有相应的spring定义");
            if(beanNames.length > 1)
                throw new RuntimeException("类:" + tClass + "有多个bean定义:" + Arrays.toString(beanNames));
            beanName = beanNames[0];
            nameMap.put(tClass, beanName);
        }

        return (T) applicationContext.getBean(tClass);
    }


}
