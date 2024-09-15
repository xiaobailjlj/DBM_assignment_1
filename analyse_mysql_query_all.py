import pymysql
import time
import matplotlib.pyplot as plt

# Function to execute the SQL query and return the execution time
def execute_query(conn, query):
    cursor = conn.cursor()
    start_time = time.time()
    cursor.execute(query)
    # Uncomment the following line if you need to fetch results
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

def run_benchmarks(conn, querys, runs=10):
    execution_times = []
    for i in range(runs):
        exec_time = 0
        for query in querys:
            exec_time += execute_query(conn, query)
            print(f"Run {i + 1}: {exec_time:.5f} seconds")
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
    plt.savefig('./results_mysql/plot_query_' + str(query_index).zfill(2) + '.png')
    plt.show()

def read_sql_file(file_path):
    with open(file_path, 'r') as file:
        sql_content = file.read()
    return sql_content

if __name__ == "__main__":
    # Connect to MonetDB (update credentials and database connection info)
    conn = pymysql.connect(user="root", passwd="lujing00", host="localhost", db="db_assignment_1")

    for query_index in range(1, 23):
        print("*** executing: q_" + str(query_index).zfill(2))

        # Number of runs to execute the query
        runs = 5

        # Define the SQL query to benchmark
        # need to break q15 to two parts
        if query_index == 15:
            query_1 = read_sql_file(
                '/Users/lujing/Desktop/cources/dbms/assignment_1/downloaded/dbgen/mysql/q' + str(query_index).zfill(
                    2) + '_1.sql')
            print(query_1)
            query_2 = read_sql_file(
                '/Users/lujing/Desktop/cources/dbms/assignment_1/downloaded/dbgen/mysql/q' + str(query_index).zfill(
                    2) + '_2.sql')
            print(query_2)

            # Run the benchmark and collect execution times(no need to run query_1 twice)
            # execution_times = run_benchmarks(conn, [query_1,query_2], runs)
            execution_times = run_benchmarks(conn, [query_2], runs)
        else:
            query = read_sql_file(
                '/Users/lujing/Desktop/cources/dbms/assignment_1/downloaded/dbgen/mysql/q' + str(query_index).zfill(
                    2) + '.sql')
            print(query)

            # Run the benchmark and collect execution times
            execution_times = run_benchmark(conn, query, runs)

        # Visualize the results
        visualize_execution_times(execution_times, query_index)

    # Close the database connection
    conn.close()