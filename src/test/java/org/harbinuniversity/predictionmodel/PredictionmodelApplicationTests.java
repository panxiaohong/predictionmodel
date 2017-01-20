package org.harbinuniversity.predictionmodel;

import com.google.common.collect.Maps;
import lombok.extern.slf4j.Slf4j;
import org.harbinuniversity.predictionmodel.util.PythonFactory;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.python.core.PyFunction;
import org.python.core.PyObject;
import org.python.core.PyString;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import java.util.HashMap;
import java.util.Map;

import static com.google.common.collect.Maps.*;

@RunWith(SpringRunner.class)
@SpringBootTest
@Slf4j
public class PredictionmodelApplicationTests {

    @Test
    public void contextLoads() {
        Map<String, Object> map = Maps.newHashMap();
        map.put("name", "leihong");
        map.put("age", 25);
        PythonFactory.getResult(PredictionmodelApplicationTests.class.getResource("/python/test.py"), "main", map,null);
    }

}
