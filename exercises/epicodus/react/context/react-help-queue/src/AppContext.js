import { createContext } from "react";

const state = {
  masterTicketList: {},
  selectedTicket: null
};

const AppContext = createContext(state); //passing initial state

export default AppContext;
