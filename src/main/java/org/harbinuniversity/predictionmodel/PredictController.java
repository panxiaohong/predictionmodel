/** created by leihong.pan at 2017/1/22 15:37 */
package org.harbinuniversity.predictionmodel;

import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 *
 *
 * @author leihong.pan
 */
@RestController
@RequestMapping("/rest/")
@Slf4j
public class PredictController {
    @RequestMapping(value = "/predict/",method = RequestMethod.GET)
    String predict(@RequestParam double lon,double lat){
        log.info("我正在执行业务方法");
        return lon+""+"==="+lat;
    }
}
