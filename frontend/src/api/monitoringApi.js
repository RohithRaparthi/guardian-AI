import axiosClient from "./axiosClient";

export const getMonitoringStatus = () => {
  return axiosClient.get("/monitoring/status");
};