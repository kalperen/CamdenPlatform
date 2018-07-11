import { Telemetry } from './telemetry';
//this class will be extended by many classes for each type of sensor
//each of this child classes will secify how to visualise itself
export class Widget {
  sensorType: string;
  sensorId: string;
  telemetries: Telemetry[];
}