ALTER TABLE session_session ADD preferred_date VARCHAR(255);
ALTER TABLE session_session ADD expected_capacity VARCHAR(255);
ALTER TABLE session_session ADD resource_space_needs VARCHAR(255);
ALTER TABLE session_session ADD rsvp_required BOOLEAN;
ALTER TABLE session_session ADD has_cost BOOLEAN;
