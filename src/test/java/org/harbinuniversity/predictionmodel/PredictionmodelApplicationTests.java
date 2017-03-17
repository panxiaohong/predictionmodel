package org.harbinuniversity.predictionmodel;

import com.google.common.collect.Maps;
import lombok.extern.slf4j.Slf4j;
import org.harbinuniversity.predictionmodel.controller.PredictController;
import org.harbinuniversity.predictionmodel.util.PythonFactory;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.Mock;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.web.servlet.MockMvc;

import java.net.URL;
import java.util.Map;

@RunWith(SpringRunner.class)
@SpringBootTest
@Slf4j
public class PredictionmodelApplicationTests {

    @Test
    public void contextLoads() {
        Map<String, Object> map = Maps.newHashMap();
        URL url = PredictionmodelApplicationTests.class.getResource("/python/datainf.py");
        map.put("lon",121.5);
        map.put("lat",35.2);
        map.put("AvgPrice",35.2);
        PythonFactory.getResult(url,"main",map);
    }

}
