import TaskForm from "./components/TaskForm";
import Tasks from "./components/Tasks";


const App = () => {
  return (
    <div>
      <h1>Task Manager (GraphQL)</h1>
      <TaskForm />
      <Tasks/>
    </div>
  );
}

export default App;
