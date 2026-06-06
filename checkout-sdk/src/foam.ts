import * as foam from '@foam-ai/browser-opentelemetry';
import { FOAM_API_KEY, IS_PRODUCTION } from './config';

foam.init({
  serviceName: 'checkout-sdk',
  isProduction: IS_PRODUCTION,
  apiKey: FOAM_API_KEY,
  sampleRate: IS_PRODUCTION ? 0.05 : 1.0,
  captureConsoleErrors: true,
});