package org.harbinuniversity.predictionmodel;

import lombok.extern.slf4j.Slf4j;
import org.harbinuniversity.predictionmodel.util.PythonFactory;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.python.core.PyFunction;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
@Slf4j
public class PredictionmodelApplicationTests {

    @Test
    public void contextLoads() {
        PyFunction pyFunction =  PythonFactory.getPyFunction(PredictionmodelApplicationTests.class
                .getResource("/python/test.py"), "main");
        log.info(pyFunction+"============");
    }

}
