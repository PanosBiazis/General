package com.example.mlaiapp.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import com.example.mlaiapp.service.ModelService;

@RestController
public class ModelController {

    @Autowired
    private ModelService modelService;

    @GetMapping("/predict")
    public String predict() {
        return modelService.getPrediction();
    }
}
