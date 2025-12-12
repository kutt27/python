"""
Python Generators: send() Method
=================================

Topic: Two-way communication with generators using send()

Real-World Applications:
- State machines
- Coroutine-style programming
- Pipeline filtering with feedback
- Interactive data processing
- Configuration updates mid-stream
"""

from typing import Generator, Optional


def moving_average() -> Generator[Optional[float], float, None]:
    """
    Calculates moving average of sent values.
    
    Yields:
        Current moving average
    
    Receives (via send):
        New value to include in average
    
    Real-world use case: Real-time metrics, sensor data smoothing.
    """
    total = 0.0
    count = 0
    average = None
    
    while True:
        # Receive new value via send()
        value = yield average
        
        total += value
        count += 1
        average = total / count


def request_processor() -> Generator[str, dict, None]:
    """
    Processes requests sent to generator.
    
    Yields:
        Processing status
    
    Receives (via send):
        Request dictionary
    
    Real-world use case: Request/response handling, command processing.
    """
    print("Request processor started")
    
    while True:
        # Wait for request
        request = yield "Waiting for request"
        
        # Process request
        if request.get("action") == "process":
            data = request.get("data", {})
            result = f"Processed: {data}"
            yield result
        elif request.get("action") == "status":
            yield "Status: Running"
        else:
            yield f"Unknown action: {request.get('action')}"


def data_filter_with_feedback() -> Generator[bool, tuple, None]:
    """
    Filters data with dynamic threshold adjustment.
    
    Yields:
        Whether value passed filter
    
    Receives (via send):
        Tuple of (value, new_threshold_optional)
    
    Real-world use case: Adaptive filtering, anomaly detection.
    """
    threshold = 100
    
    while True:
        # Receive (value, optional new threshold)
        data = yield
        
        if isinstance(data, tuple):
            value, *rest = data
            
            # Update threshold if provided
            if rest and rest[0] is not None:
                threshold = rest[0]
                print(f"  Threshold updated to: {threshold}")
            
            # Check if value passes filter
            passed = value > threshold
            yield passed
        else:
            yield False


def stateful_counter() -> Generator[int, str, None]:
    """
    Counter that responds to commands.
    
    Yields:
        Current count
    
    Receives (via send):
        Command string ("inc", "dec", "reset")
    
    Real-world use case: Interactive state management.
    """
    count = 0
    
    while True:
        command = yield count
        
        if command == "inc":
            count += 1
        elif command == "dec":
            count -= 1
        elif command == "reset":
            count = 0
        elif command:
            print(f"  Unknown command: {command}")


def pipeline_stage(name: str) -> Generator[dict, dict, None]:
    """
    Pipeline stage that processes and forwards data.
    
    Args:
        name: Stage name
    
    Yields:
        Processed data
    
    Receives (via send):
        Input data
    
    Real-world use case: ETL pipelines, data transformation chains.
    """
    processed_count = 0
    
    while True:
        data = yield
        
        # Process data
        processed_data = {
            **data,
            f"{name}_processed": True,
            f"{name}_timestamp": f"T{processed_count}"
        }
        
        processed_count += 1
        
        yield processed_data


def main() -> None:
    """Main function demonstrating send() method."""
    print("="*70)
    print("GENERATOR send() METHOD".center(70))
    print("="*70)
    
    print("\n[1] MOVING AVERAGE CALCULATOR")
    print("-" * 70)
    
    avg_gen = moving_average()
    next(avg_gen)  # Prime the generator
    
    values = [10, 20, 30, 40, 50]
    
    print("Calculating moving average:")
    for value in values:
        avg = avg_gen.send(value)
        print(f"  Added {value} → Average: {avg:.2f}")
    
    print("\n\n[2] REQUEST PROCESSOR")
    print("-" * 70)
    
    processor = request_processor()
    print(next(processor))  # Start processor
    
    # Send requests
    requests = [
        {"action": "process", "data": {"user_id": 101}},
        {"action": "status"},
        {"action": "process", "data": {"order_id": "ORD-123"}},
    ]
    
    for req in requests:
        response = processor.send(req)
        print(f"Request: {req['action']} → Response: {response}")
        if response != "Waiting for request":
            next(processor)  # Continue to next wait state
    
    print("\n\n[3] ADAPTIVE DATA FILTER")
    print("-" * 70)
    
    data_filter = data_filter_with_feedback()
    next(data_filter)  # Prime
    
    # Test data with optional threshold updates
    test_data = [
        (150, None),     # Use current threshold (100)
        (75, None),      # Use current threshold
        (120, 110),      # Update threshold to 110
        (105, None),     # Use new threshold (110)
        (115, None),     # Use new threshold
    ]
    
    print("Filtering data (initial threshold: 100):")
    for value, new_threshold in test_data:
        passed = data_filter.send((value, new_threshold))
        next(data_filter)  # Get result
        status = "✓ Passed" if passed else "✗ Blocked"
        print(f"  Value {value}: {status}")
    
    print("\n\n[4] STATEFUL COUNTER")
    print("-" * 70)
    
    counter = stateful_counter()
    next(counter)  # Prime
    
    commands = ["inc", "inc", "inc", "dec", "reset", "inc"]
    
    print("Counter commands:")
    for cmd in commands:
        count = counter.send(cmd)
        print(f"  Command '{cmd}' → Count: {count}")
    
    print("\n\n[5] DATA PIPELINE")
    print("-" * 70)
    
    # Create pipeline stages
    stage1 = pipeline_stage("validation")
    stage2 = pipeline_stage("enrichment")
    
    # Prime stages
    next(stage1)
    next(stage2)
    
    # Process data through pipeline
    input_data = {"user_id": 101, "action": "login"}
    
    print(f"Input: {input_data}")
    
    # Stage 1
    result1 = stage1.send(input_data)
    next(stage1)
    print(f"After stage 1: {result1}")
    
    # Stage 2
    result2 = stage2.send(result1)
    next(stage2)
    print(f"After stage 2: {result2}")
    
    print("\n" + "="*70)
    print("Generator send() Method:")
    print("-" * 70)
    print("Syntax:")
    print("  gen = my_generator()")
    print("  next(gen)              # Prime the generator")
    print("  result = gen.send(value)  # Send value, get result")
    print("\nKey Points:")
    print("• send() both sends a value AND resumes generator")
    print("• Must call next() first to prime generator")
    print("• Value sent becomes result of yield expression")
    print("• Enables two-way communication")
    print("\nCommon Pattern:")
    print("  value = yield result")
    print("  # value comes from send()")
    print("  # result is what send() returns")
    print("\nUse Cases:")
    print("✓ State machines")
    print("✓ Coroutines")
    print("✓ Interactive data processing")
    print("✓ Pipeline stages with feedback")
    print("✓ Real-time metric calculation")
    print("="*70)


if __name__ == "__main__":
    main()