# Bouncing balls: Earth to Mars

A 15-minute coding activity for high school students. Build a ball, replace fake gravity with time-based physics, add bouncing, compare ball sizes, and move to Mars.

Open https://editor.p5js.org/ in Safari. Replace everything in `sketch.js` with the code for the current stage, then click ▶ Run. Click Stop and Run to reset an experiment. The lesson file itself works offline; the online p5.js editor needs internet access.

For a tight 15-minute session, use the complete code as a checkpoint and have students focus on changing the key lines. No libraries need to be added to the default p5.js sketch.

## 1. Fake gravity: move every frame

**0–3 minutes**

Start with the code below. Click Run. The ball moves down and eventually disappears; click Stop, then Run to restart it.

The screen’s y coordinate increases downward. `circle(200, y, 40)` draws a ball at x = 200, with diameter 40 pixels. `draw()` runs repeatedly, once per frame.

**Try:** Change `frameRate(60)` to `frameRate(30)` and restart. At 60 frames per second, 3 pixels per frame means 180 pixels per second. At 30 frames per second, it means 90 pixels per second. These are target frame rates; the computer may run slower.

**Ask:** Does a dropped ball really fall at a constant speed? Why did changing the frame rate change our ball’s motion?

```javascript
let y = 60;

function setup() {
  createCanvas(600, 420);
  frameRate(60);
}

function draw() {
  background(235);
  y += 3; // Move 3 pixels every frame
  fill("orange");
  circle(200, y, 40);
}
```

## 2. Real acceleration and frame rate

**3–7 minutes**

Replace the code with this version. Gravity now changes speed over time. Speed changes position.

`deltaTime` gives the previous frame’s duration in milliseconds. Dividing by 1000 gives seconds. A frame lasting 1/30 of a second advances the motion twice as far in time as one lasting 1/60 of a second.

The position calculation is **distance = speed × time + ½ × acceleration × time²**. Then we update speed using **speed += acceleration × time**. This gives the correct constant-acceleration motion between collisions, regardless of how we divide time into frames.

We use Earth gravity of about 9.81 m/s² and a drawing scale of 50 pixels per metre. That makes the acceleration 490.5 pixels/s².

**Try:** Compare `frameRate(30)` and `frameRate(60)`, restarting each time. The fall should take about the same real time, although 60 FPS looks smoother. Restore 60 FPS afterward.

**Ask:** What is the difference between moving the same distance each frame and moving according to elapsed time?

```javascript
let y = 60;
let speed = 0;           // Pixels per second
let gravity = 9.81 * 50; // Earth: m/s² × 50 pixels per metre

function setup() {
  createCanvas(600, 420);
  frameRate(60);
}

function draw() {
  background(235);
  let dt = deltaTime / 1000; // Milliseconds → seconds

  y += speed * dt + 0.5 * gravity * dt * dt;
  speed += gravity * dt;

  fill("orange");
  circle(200, y, 40);
}
```

## 3. Make it bounce

**7–10 minutes**

Add the `if` block below the speed update, or replace the whole sketch with this version.

The ball’s centre reaches the floor at `height - 20`, because its radius is 20 pixels. We place it back above the floor and reverse its downward speed. Multiplying by 0.85 keeps 85% of its impact speed, so it loses energy at each bounce. The `speed > 0` check means “only while moving downward.”

**Try:** Change `0.85` to `1` for a nearly elastic bounce, or `0.5` for a less bouncy ball.

**Ask:** Why do we reverse speed instead of reversing gravity?

**Teacher note:** Collision detection happens once per frame. The floor correction is approximate, so bounce heights can differ a little with frame rate, and the ball may jitter when nearly stopped. A production physics engine would handle impact timing and resting contacts more carefully. Avoid leaving the running sketch in a background tab; restart it when returning.

```javascript
let y = 60;
let speed = 0;           // Pixels per second
let gravity = 9.81 * 50; // Earth: m/s² × 50 pixels per metre

function setup() {
  createCanvas(600, 420);
  frameRate(60);
}

function draw() {
  background(235);
  let dt = deltaTime / 1000; // Milliseconds → seconds

  y += speed * dt + 0.5 * gravity * dt * dt;
  speed += gravity * dt;

  if (y >= height - 20 && speed > 0) {
    y = height - 20;
    speed = -speed * 0.85;
  }

  fill("orange");
  circle(200, y, 40);
}
```

## 4. Add a green ball, twice the diameter

**10–13 minutes**

Keep the orange ball and add a green ball with diameter 80 pixels. Both use the same gravity and bounce value, but each has its own position and speed.

The green ball starts at y = 40 and the orange ball at y = 60. Their bottom edges both start at y = 80, so they have the same distance to fall before touching the floor. The green ball touches the floor when its centre reaches `height - 40`.

**Predict before running:** Which will hit the floor first?

**Discuss:** They land together in this model. Size alone does not change gravitational acceleration; we are ignoring air resistance. “Twice the size” here means twice the diameter, not twice the mass. If we started both centres at the same height, the larger ball would touch first simply because its bottom is lower.

```javascript
let y = 60;
let speed = 0;
let greenY = 40; // Same starting bottom edge: 80 pixels
let greenSpeed = 0;
let gravity = 9.81 * 50; // 50 pixels represents one metre
let bounce = 0.85;

function setup() {
  createCanvas(600, 420);
  frameRate(60);
}

function draw() {
  background(235);
  let dt = deltaTime / 1000;

  // Orange ball: diameter 40, radius 20
  y += speed * dt + 0.5 * gravity * dt * dt;
  speed += gravity * dt;
  if (y >= height - 20 && speed > 0) {
    y = height - 20;
    speed = -speed * bounce;
  }

  // Green ball: diameter 80, radius 40
  greenY += greenSpeed * dt + 0.5 * gravity * dt * dt;
  greenSpeed += gravity * dt;
  if (greenY >= height - 40 && greenSpeed > 0) {
    greenY = height - 40;
    greenSpeed = -greenSpeed * bounce;
  }

  fill("orange");
  circle(200, y, 40);
  fill("green");
  circle(400, greenY, 80);
}
```

## 5. Bounce on Mars

**13–15 minutes**

Change just the gravity line to `let gravity = 3.71 * 50;`. Keep the same drawing scale, initial positions, and bounce value. The full version below also changes the background to a sandy colour.

Mars gravity is about 3.71 m/s², roughly 38% of Earth’s gravity.

**Predict:** Will the balls fall more slowly? Will the green ball now fall faster than the orange one?

**Observe:** Both fall more slowly, and each bounce takes longer. Both balls still share the same acceleration.

**Useful surprise:** Dropping a ball from the same height on Mars does not automatically give a higher rebound. It hits the ground more slowly, too. With the same bounce factor, the ideal rebound height above contact is the same fraction of its drop height: 0.85² ≈ 72%. The animation’s approximate floor collision can introduce small differences. A ball launched upward at the same initial speed would reach higher on Mars.

```javascript
let y = 60;
let speed = 0;
let greenY = 40; // Same starting bottom edge: 80 pixels
let greenSpeed = 0;
let gravity = 3.71 * 50; // Mars gravity; same scale as Earth
let bounce = 0.85;

function setup() {
  createCanvas(600, 420);
  frameRate(60);
}

function draw() {
  background(245, 220, 205);
  let dt = deltaTime / 1000;

  // Orange ball: diameter 40, radius 20
  y += speed * dt + 0.5 * gravity * dt * dt;
  speed += gravity * dt;
  if (y >= height - 20 && speed > 0) {
    y = height - 20;
    speed = -speed * bounce;
  }

  // Green ball: diameter 80, radius 40
  greenY += greenSpeed * dt + 0.5 * gravity * dt * dt;
  greenSpeed += gravity * dt;
  if (greenY >= height - 40 && greenSpeed > 0) {
    greenY = height - 40;
    greenSpeed = -greenSpeed * bounce;
  }

  fill("orange");
  circle(200, y, 40);
  fill("green");
  circle(400, greenY, 80);
}
```

## Sources

- p5.js deltaTime: https://p5js.org/reference/p5/deltaTime/
- p5.js frameRate: https://p5js.org/reference/p5/frameRate/
- NASA classroom activity with Earth and Mars gravity values: https://mars.nasa.gov/files/mep/robotics_activities.pdf
- ESA Mars facts: https://www.esa.int/Science_Exploration/Space_Science/Mars_Express/Facts_about_Mars
