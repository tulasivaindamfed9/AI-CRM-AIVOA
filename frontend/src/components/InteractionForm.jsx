import "../styles/form.css";
import { useSelector } from "react-redux";

function InteractionForm() {
  const interaction = useSelector((state) => state.interaction);

  return (
    <div className="form-card">
      <h5 className="mb-4">Interaction Details</h5>
{/* change all the field names to snake_case */}
      <div className="mb-3">
        <label className="form-label">HCP Name</label>
        <input
          type="text"
          className="form-control"
          value={interaction.hcp_name}
          readOnly
        />
      </div>

      <div className="mb-3">
        <label className="form-label">Interaction Type</label>
        <input
          type="text"
          className="form-control"
          value={interaction.interaction_type}
          readOnly
        />
      </div>

      <div className="mb-3">
        <label className="form-label">Date</label>
        <input
          type="text"
          className="form-control"
          value={interaction.date}
          readOnly
        />
      </div>

      <div className="mb-3">
        <label className="form-label">Time</label>
        <input
          type="text"
          className="form-control"
          value={interaction.time}
          readOnly
        />
      </div>

      <div className="mb-3">
        <label className="form-label">Attendees</label>
        <input
          type="text"
          className="form-control"
          value={interaction.attendees}
          readOnly
        />
      </div>

      <div className="mb-3">
        <label className="form-label">Topics Discussed</label>
        <textarea
          className="form-control"
          rows="4"
          value={interaction.topics_discussed}
          readOnly
        />
      </div>

      <div className="mb-3">
        <label className="form-label">Materials Shared</label>
        <textarea
          className="form-control"
          rows="2"
          value={interaction.materials_shared}
          readOnly
        />
      </div>

      <div className="mb-3">
        <label className="form-label">Samples Distributed</label>
        <textarea
          className="form-control"
          rows="2"
          value={interaction.samples_distributed}
          readOnly
        />
      </div>

      <div className="mb-3">
        <label className="form-label">Sentiment</label>
        <input
          type="text"
          className="form-control"
          value={interaction.sentiment}
          readOnly
        />
      </div>

      <div className="mb-3">
        <label className="form-label">Outcomes</label>
        <textarea
          className="form-control"
          rows="3"
          value={interaction.outcomes}
          readOnly
        />
      </div>

      <div className="mb-3">
        <label className="form-label">Follow-up Actions</label>
        <textarea
          className="form-control"
          rows="3"
          value={interaction.follow_up_actions}
          readOnly
        />
      </div>

      <div className="mb-3">
        <label className="form-label">AI Suggested Follow-ups</label>
        <ul className="mb-0">
          {interaction.ai_suggestions.length > 0 ? (
            interaction.ai_suggestions.map((item, index) => (
              <li key={index}>{item}</li>
            ))
          ) : (
            <li>No suggestions available.</li>
          )}
        </ul>
      </div>
    </div>
  );
}

export default InteractionForm;