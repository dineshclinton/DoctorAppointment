import axios from "axios";

export const fetchClinicians = async () => {
  const response = await axios.get("/clinicians/");
  return response.data;
};
