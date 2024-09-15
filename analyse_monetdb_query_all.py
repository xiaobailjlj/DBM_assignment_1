import pymonetdb
import time
import matplotlib.pyplot as plt

# Function to execute the SQL query and return the execution time
def execute_query(conn, query):
    cursor = conn.cursor()
    start_time = time.time()
    cursor.execute(query)
    # cursor.fetchall()
    end_time = time.time()
    cursor.close()
    return end_time - start_time

# Function to run the query multiple times and record execution times
def run_benchmark(conn, query, runs=10):
    execution_times = []
    for i in range(runs):
        exec_time = execute_query(conn, query)
        print(f"Run {i+1}: {exec_time:.5f} seconds")
        execution_times.append(exec_time)
    return execution_times

# Visualize the execution times using matplotlib
def visualize_execution_times(execution_times, query_index):
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(execution_times) + 1), execution_times, marker='o', linestyle='-', color='b')
    plt.title('SQL Query ' + str(query_index).zfill(2) + ' Execution Times Over Multiple Runs')
    plt.xlabel('Run Number')
    plt.ylabel('Execution Time (seconds)')
    plt.grid(True)
    plt.savefig('./results_monetdb/plot_query_' + str(query_index).zfill(2) + '.png')
    plt.show()

def read_sql_file(file_path):
    with open(file_path, 'r') as file:
        sql_content = file.read()
    return sql_content

if __name__ == "__main__":
    # Connect to MonetDB (update credentials and database connection info)
    conn = pymonetdb.connect(username="monetdb", password="monetdb", hostname="localhost", database="db_assignment_1")

    for query_index in range(1, 23):
        # Define the SQL query to benchmark
        query = read_sql_file('./MonetDB/q' + str(query_index).zfill(2) + '.sql')
        print(query)

        # Number of runs to execute the query
        runs = 10

        # Run the benchmark and collect execution times
        execution_times = run_benchmark(conn, query, runs)

        # Visualize the results
        visualize_execution_times(execution_times, query_index)

    # Close the database connection
    conn.close()