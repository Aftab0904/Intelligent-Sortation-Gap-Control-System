import math

class DynamicGapController:
    """
    Advanced Gap Control for Fragile Goods.
    Adjusts speed based on momentum and package sensitivity.
    """
    def __init__(self, target_throughput_cph=2100):
        self.belt_speed = 1.8 # m/s
        self.min_safe_gap = 0.5 # meters
        self.fragile_acceleration_limit = 0.8 # m/s^2

    def calculate_merge_velocity(self, main_line_gap, feeder_line_package_pos):
        """
        Logic to merge a package from a feeder line into a gap on the main line.
        """
        if main_line_gap > self.min_safe_gap:
            # Calculate if feeder package can reach merge point in time
            required_accel = (2 * (main_line_gap / 2)) / (1.0**2) 
            
            if required_accel <= self.fragile_acceleration_limit:
                return {"status": "EXECUTE_MERGE", "speed_adj": required_accel}
            else:
                return {"status": "HOLD_FEEDER", "reason": "ACCEL_TOO_HIGH_FOR_FRAGILE"}
        
        return {"status": "WAIT_FOR_GAP"}

    def monitor_io_link_feedback(self, sensor_data):
        """
        Simulates reading IO-Link data to detect package slippage.
        """
        actual_pos = sensor_data['actual']
        expected_pos = sensor_data['expected']
        
        drift = actual_pos - expected_pos
        if abs(drift) > 0.05: # 5cm drift
            return f"[CORRECTION] Adjusting upstream VFD to compensate for {drift}m slippage."
        return "[OK] Tracking within tolerance."

if __name__ == "__main__":
    controller = DynamicGapController()
    print("Intelligent Merge Controller Active...")
    
    # Simulate a merge decision
    decision = controller.calculate_merge_velocity(main_line_gap=0.8, feeder_line_package_pos=0)
    print(f"Merge Decision: {decision}")
    
    # Simulate slippage detection
    correction = controller.monitor_io_link_feedback({'actual': 10.58, 'expected': 10.50})
    print(correction)
