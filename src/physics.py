def dot_product(v1, v2):
    """Calculate the dot product of two vectors."""
    return v1[0] * v2[0] + v1[1] * v2[1]

def scalar_multiply(scalar, vector):
    """Multiply a vector by a scalar."""
    return [scalar * vector[0], scalar * vector[1]]

def detet_collision(ball_1, ball_2):
    """Detect collision between two balls."""
    dx = ball_2.position[0] - ball_1.position[0]
    dy = ball_2.position[1] - ball_1.position[1]
    distance = (dx**2 + dy**2)**0.5
    return distance <= ball_1.radius + ball_2.radius

def resolve_collision(ball_1, ball_2):
    """Resolve collision between two balls."""
    dx = ball_2.position[0] - ball_1.position[0]
    dy = ball_2.position[1] - ball_1.position[1]
    distance = (dx**2 + dy**2)**0.5

    # Normal vector
    eps = 1e-6
    if distance < eps:
        nx, ny = 1.0, 0.0
        distance = eps
    else:
        nx = dx / distance
        ny = dy / distance

    # Scalar projections (dot products)
    v1n = dot_product(ball_1.velocity, [nx, ny])
    v2n = dot_product(ball_2.velocity, [nx, ny])

    # Tangential components
    p1_t = [ball_1.velocity[0] - v1n * nx,
            ball_1.velocity[1] - v1n * ny]

    p2_t = [ball_2.velocity[0] - v2n * nx,
            ball_2.velocity[1] - v2n * ny]

    # New normal components after collision (elastic collision)
    m1, m2 = ball_1.mass, ball_2.mass
    v1n_new = (v1n * (m1 - m2) + 2 * m2 * v2n) / (m1 + m2)
    v2n_new = (v2n * (m2 - m1) + 2 * m1 * v1n) / (m1 + m2)

    # Update velocities
    ball_1.velocity = [p1_t[0] + v1n_new * nx,
                       p1_t[1] + v1n_new * ny]

    ball_2.velocity = [p2_t[0] + v2n_new * nx,
                       p2_t[1] + v2n_new * ny]
    
    # Adjust positions to prevent overlap
    overlap = (ball_1.radius + ball_2.radius) - distance
    if overlap > 0:
        correction_x = (overlap / 2.0) * nx
        correction_y = (overlap / 2.0) * ny
        ball_1.position[0] -= correction_x
        ball_1.position[1] -= correction_y
        ball_2.position[0] += correction_x
        ball_2.position[1] += correction_y

def handle_ball_collision(ball1, ball2):
    """Check and handle collision between two balls."""
    if detet_collision(ball1, ball2):
        resolve_collision(ball1, ball2)