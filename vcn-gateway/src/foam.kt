package com.affirm.vcn

import ai.foam.opentelemetry.FoamSdk
import ai.foam.opentelemetry.FoamConfig
import org.springframework.beans.factory.annotation.Value
import org.springframework.context.annotation.Configuration
import javax.annotation.PostConstruct

@Configuration
class FoamConfiguration {
    @Value("\${foam.api.key}")
    private lateinit var apiKey: String

    @Value("\${spring.profiles.active}")
    private lateinit var activeProfile: String

    @PostConstruct
    fun initFoam() {
        FoamSdk.init(
            FoamConfig(
                serviceName = "vcn-gateway",
                apiKey = apiKey,
                isProduction = activeProfile == "production"
            )
        )
    }
}