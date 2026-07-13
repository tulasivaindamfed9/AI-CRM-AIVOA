import Header from "../components/Header";
import InteractionForm from "../components/InteractionForm";
import ChatPanel from "../components/ChatPanel";

import "../styles/app.css";

function LogInteraction() {
  return (
    <>
      <Header />

      <div className="container mt-4">

        <div className="row">

          <div className="col-lg-8 mb-3">
            <InteractionForm />
          </div>

          <div className="col-lg-4">
            <ChatPanel />
          </div>

        </div>

      </div>
    </>
  );
}

export default LogInteraction;