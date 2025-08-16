import { useQuery, gql } from "@apollo/client";

// Define GraphQL query
const GET_TASKS = gql`
  query GetTasks {
    allTasks {
      id
      title
      completed
    }
  }
`;

export {GET_TASKS}

function Tasks() {
  const { loading, error, data } = useQuery(GET_TASKS);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error 😢 {error.message}</p>;

  return (
    <ul>
      {data.allTasks.map((task) => (
        <li key={task.id}>
          {task.title} - {task.completed ? "✅ Done" : "❌ Not Done"}
        </li>
      ))}
    </ul>
  );
}

export default Tasks;
