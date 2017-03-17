/** created by leihong.pan at 2017/1/22 15:37 */
package org.harbinuniversity.predictionmodel.controller;

import lombok.extern.slf4j.Slf4j;
import org.harbinuniversity.predictionmodel.service.PredictService;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.Resource;
import java.util.ArrayList;
import java.util.List;

/**
 *
 *
 * @author leihong.pan
 */
@RestController
@RequestMapping("/rest")
@Slf4j
public class PredictController {

    @Resource
    PredictService predictService;

    @RequestMapping(value = "/predict/",method = RequestMethod.GET)
    public String predict(@RequestParam double lon,@RequestParam double lat,@RequestParam double avgPrice){
       return predictService.predict(lon,lat,avgPrice);
    }
}
