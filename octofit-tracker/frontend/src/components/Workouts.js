import React, { useEffect, useState } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch('https://[REPLACE-THIS-WITH-YOUR-CODESPACE-NAME]-8000.app.github.dev/api/workouts/')
      .then(response => response.json())
      .then(data => setWorkouts(data))
      .catch(error => console.error('Error fetching workouts:', error));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="text-center mb-4">Workouts</h1>
      <ul className="list-group">
        {workouts.map(workout => (
          <li key={workout._id} className="list-group-item">
            <strong>{workout.name}</strong>: {workout.description}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Workouts;
