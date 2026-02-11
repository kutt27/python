"""
Demonstrates floor division (//) and modulo (%) operations.
"""

def demonstrate_floor_division_modulo() -> None:
    # Example: Distributing 1000 records across 6 worker processes
    total_records = 1000
    worker_processes = 6
    
    # Floor division: Records per worker
    records_per_worker = total_records // worker_processes
    print(f"Records per worker: {records_per_worker}")
    print(f"Calculation: {total_records} // {worker_processes} = {records_per_worker}")
    
    # Modulo: Remaining records
    remaining_records = total_records % worker_processes
    print(f"Remaining records: {remaining_records}")
    print(f"Calculation: {total_records} % {worker_processes} = {remaining_records}")

if __name__ == "__main__":
    demonstrate_floor_division_modulo()
