/** created by leihong.pan at 2017/2/6 14:02 */
package org.harbinuniversity.predictionmodel.service;

import com.google.common.collect.Maps;
import org.harbinuniversity.predictionmodel.util.PythonFactory;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.Map;

/**
 *
 *
 * @author leihong.pan
 */
@Service
public class PredictService {

   public String predict(double lon,  double lat, double avgPrice){
       Map<String,Object> params = Maps.newHashMap();
       params.put("lon",lon);
       params.put("lat",lat);
       params.put("avgPrice",avgPrice);
       return PythonFactory.getResult("main",params).toString();
   };
}
