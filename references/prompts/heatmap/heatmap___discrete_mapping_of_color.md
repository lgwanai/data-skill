## 图表类型：热力图 - 颜色的离散映射 (Heatmap - Discrete Mapping of Color)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
let noise = getNoiseHelper();
let xData = [];
let yData = [];
noise.seed(Math.random());
function generateData(theta, min, max) {
  let data = [];
  for (let i = 0; i <= 200; i++) {
    for (let j = 0; j <= 100; j++) {
      // let x = (max - min) * i / 200 + min;
      // let y = (max - min) * j / 100 + min;
      data.push([i, j, noise.perlin2(i / 40, j / 20) + 0.5]);
      // data.push([i, j, normalDist(theta, x) * normalDist(theta, y)]);
    }
    xData.push(i);
  }
  for (let j = 0; j < 100; j++) {
    yData.push(j);
  }
  return data;
}
let data = generateData(2, -5, 5);
option = {
  tooltip: {},
  grid: {
    right: 140,
    left: 40
  },
  xAxis: {
    type: 'category',
    data: xData
  },
  yAxis: {
    type: 'category',
    data: yData
  },
  visualMap: {
    type: 'piecewise',
    min: 0,
    max: 1,
    left: 'right',
    top: 'center',
    calculable: true,
    realtime: false,
    splitNumber: 8,
    inRange: {
      color: [ /* 请使用用户的真实数据数组替换此处 */ ]
    }
  },
  series: [
    {
      name: 'Gaussian',
      type: 'heatmap',
      data: data,
      emphasis: {
        itemStyle: {
          borderColor: '#333',
          borderWidth: 1
        }
      },
      progressive: 1000,
      animation: false
    }
  ]
};
///////////////////////////////////////////////////////////////////////////
// perlin noise helper from https://github.com/josephg/noisejs
///////////////////////////////////////////////////////////////////////////
function getNoiseHelper() {
  class Grad {
    constructor(x, y, z) {
      this.x = x;
      this.y = y;
      this.z = z;
    }
    dot2(x, y) {
      return this.x * x + this.y * y;
    }
    dot3(x, y, z) {
      return this.x * x + this.y * y + this.z * z;
    }
  }
  const grad3 = [
    new Grad(1, 1, 0),
    new Grad(-1, 1, 0),
    new Grad(1, -1, 0),
    new Grad(-1, -1, 0),
    new Grad(1, 0, 1),
    new Grad(-1, 0, 1),
    new Grad(1, 0, -1),
    new Grad(-1, 0, -1),
    new Grad(0, 1, 1),
    new Grad(0, -1, 1),
    new Grad(0, 1, -1),
    new Grad(0, -1, -1)
  ];
  const p = [ /* 请使用用户的真实数据数组替换此处 */ ];
  // To remove the need for index wrapping, double the permutation table length
  let perm = new Array(512);
  let gradP = new Array(512);
  // This isn't a very good seeding function, but it works ok. It supports 2^16
  // different seed values. Write something better if you need more seeds.
  function seed(seed) {
    if (seed > 0 && seed < 1) {
      // Scale the seed out
      seed *= 65536;
    }
    seed = Math.floor(seed);
    if (seed < 256) {
      seed |= seed << 8;
    }
    for (let i = 0; i < 256; i++) {
      let v;
      if (i & 1) {
        v = p[i] ^ (seed & 255);
      } else {
        v = p[i] ^ ((seed >> 8) & 255);
      }
      perm[i] = perm[i + 256] = v;
      gradP[i] = gradP[i + 256] = grad3[v % 12];
    }
  }
  seed(0);
  // ##### Perlin noise stuff
  function fade(t) {
    return t * t * t * (t * (t * 6 - 15) + 10);
  }
  function lerp(a, b, t) {
    return (1 - t) * a + t * b;
  }
  // 2D Perlin Noise
  function perlin2(x, y) {
    // Find unit grid cell containing point
    let X = Math.floor(x),
      Y = Math.floor(y);
    // Get relative xy coordinates of point within that cell
    x = x - X;
    y = y - Y;
    // Wrap the integer cells at 255 (smaller integer period can be introduced here)
    X = X & 255;
    Y = Y & 255;
    // Calculate noise contributions from each of the four corners
    let n00 = gradP[X + perm[Y]].dot2(x, y);
    let n01 = gradP[X + perm[Y + 1]].dot2(x, y - 1);
    let n10 = gradP[X + 1 + perm[Y]].dot2(x - 1, y);
    let n11 = gradP[X + 1 + perm[Y + 1]].dot2(x - 1, y - 1);
    // Compute the fade curve value for x
    let u = fade(x);
    // Interpolate the four results
    return lerp(lerp(n00, n10, u), lerp(n01, n11, u), fade(y));
  }
  return {
    seed,
    perlin2
  };
}
```

