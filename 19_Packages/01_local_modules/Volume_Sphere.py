class volume_Sphere:
    def __init__(self, part: float ,pi: float , radius: float):
     
        self.partpart = part
        self.pi = pi
        self.radius = radius
    def __str__(self):
        return f"volume_Sphere {self.part} x {self.pi} x {self.radius**3}"