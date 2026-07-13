import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const logInteraction = (message) => {
  return api.post("/interaction/log", {
    message,
  });
};


export const editInteraction = (message) => {
  return api.put("/interaction/edit", {
    message,
  });
};


export default api;

