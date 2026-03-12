import axiosClient from "./axiosClient";

export const registerGuardian = (data) => {
  return axiosClient.post("/guardians", data);
};