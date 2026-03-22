## 图表类型：动态数据 (Dynamic Data)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
const categories = (function () {
  let now = new Date();
  let res = [];
  let len = 10;
  while (len--) {
    res.unshift(now.toLocaleTimeString().replace(/^\D*/, ''));
    now = new Date(+now - 2000);
  }
  return res;
})();
const categories2 = (function () {
  let res = [];
  let len = 10;
  while (len--) {
    res.push(10 - len - 1);
  }
  return res;
})();
const data = (function () {
  let res = [];
  let len = 10;
  while (len--) {
    res.push(Math.round(Math.random() * 1000));
  }
  return res;
})();
const data2 = (function () {
  let res = [];
  let len = 0;
  while (len < 10) {
    res.push(+(Math.random() * 10 + 5).toFixed(1));
    len++;
  }
  return res;
})();
option = {
  title: {
    text: 'Dynamic Data'
  },
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'cross',
      label: {
        backgroundColor: '#283b56'
      }
    }
  },
  legend: {},
  toolbox: {
    show: true,
    feature: {
      dataView: { readOnly: false },
      restore: {},
      saveAsImage: {}
    }
  },
  dataZoom: {
    show: false,
    start: 0,
    end: 100
  },
  xAxis: [
    {
      type: 'category',
      boundaryGap: true,
      data: categories
    },
    {
      type: 'category',
      boundaryGap: true,
      data: categories2
    }
  ],
  yAxis: [
    {
      type: 'value',
      scale: true,
      name: 'Price',
      max: 30,
      min: 0,
      boundaryGap: [0.2, 0.2]
    },
    {
      type: 'value',
      scale: true,
      name: 'Order',
      max: 1200,
      min: 0,
      boundaryGap: [0.2, 0.2]
    }
  ],
  series: [
    {
      name: 'Dynamic Bar',
      type: 'bar',
      xAxisIndex: 1,
      yAxisIndex: 1,
      data: data
    },
    {
      name: 'Dynamic Line',
      type: 'line',
      data: data2
    }
  ]
};
app.count = 11;
setInterval(function () {
  let axisData = new Date().toLocaleTimeString().replace(/^\D*/, '');
  data.shift();
  data.push(Math.round(Math.random() * 1000));
  data2.shift();
  data2.push(+(Math.random() * 10 + 5).toFixed(1));
  categories.shift();
  categories.push(axisData);
  categories2.shift();
  categories2.push(app.count++);
  myChart.setOption({
    xAxis: [
      {
        data: categories
      },
      {
        data: categories2
      }
    ],
    series: [
      {
        data: data
      },
      {
        data: data2
      }
    ]
  });
}, 2100);
```

