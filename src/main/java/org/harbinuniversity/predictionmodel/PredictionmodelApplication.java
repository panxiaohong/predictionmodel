package org.harbinuniversity.predictionmodel;

import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.web.servlet.ServletComponentScan;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@SpringBootApplication
@Slf4j
@ServletComponentScan
@Controller
public class PredictionmodelApplication {


	/** index.html*/
	@RequestMapping("/")
	public String  index(){
		return "index";
	}

	public static void main(String[] args) {
		SpringApplication.run(PredictionmodelApplication.class, args);
	}
}
