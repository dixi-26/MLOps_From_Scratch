class MLOpsWhileAlgorithms:
    def check_convergence(self, starting_loss: float, reduction_rate: float, target_loss: float) -> int:
        iterations = 0
        current_loss = starting_loss
        while current_loss > target_loss:
            current_loss -= reduction_rate
            iterations += 1
        return iterations
    def drain_buffer(self, initial_buffer_size: int, stream_packets: list) -> int:
        buffer_pool = initial_buffer_size
        idx = 0
        while buffer_pool > 0 and idx < len(stream_packets):
            packet = stream_packets[idx]
            if packet == 0:  # Corrupted packet found
                break
            buffer_pool -= packet
            idx += 1
        return max(0, buffer_pool)
runner = MLOpsWhileAlgorithms()
print("P1 Iterations to Target:", runner.check_convergence(1.5, 0.2, 0.5))
print("P2 Remaining RAM Buffer:", runner.drain_buffer(500, [50, 100, 0, 50]))