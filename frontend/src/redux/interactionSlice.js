import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  id: null,
  hcp_name: "",
  interaction_type: "",
  date: "",
  time: "",
  attendees: "",
  topics_discussed: "",
  materials_shared: "",
  samples_distributed: "",
  sentiment: "",
  outcomes: "",
  follow_up_actions: "",
  ai_suggestions: "",
};

const interactionSlice = createSlice({
  name: "interaction",
  initialState,
  reducers: {
    setInteraction(state, action) {
      return { ...state, ...action.payload };
    },

    clearInteraction() {
      return initialState;
    },
  },
});

export const { setInteraction, clearInteraction } =
  interactionSlice.actions;

export default interactionSlice.reducer;