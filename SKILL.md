---
name: douyin-title-generator
description: Generate eye-catching viral titles for Douyin (TikTok) content to improve click-through rates and engagement.
metadata:
  {
    "openclaw":
      {
        "emoji": "🎯",
        "requires": { "bins": ["python3"], "env": [] }
      },
  }
---
# Douyin Title Generator

Generate eye-catching viral titles for Douyin (TikTok) content to improve click-through rates and engagement.

## Trigger Conditions

Activate this skill when the user mentions:
- douyin title generation
- douyin viral titles
- douyin video titles
- 抖音标题生成
- 抖音爆款标题
- 抖音视频标题

## Features

- Diverse title templates (10+ different styles)
- Intelligent emotional word matching
- Automatic popular emoji addition
- Customizable product types and keywords
- Batch generation of multiple titles for selection
- Optimized for e-commerce products (bedding, clothing, cosmetics, etc.)

## Usage

### Basic Usage
```bash
# Generate titles for specified product type
douyin-title-generator bedding

# Generate titles with specific keywords
douyin-title-generator bedding sheets,cotton,duvet

# Specify number of titles to generate
douyin-title-generator bedding sheets,cotton 10
```

### Parameters
- `product_type`: Required parameter (e.g., "bedding", "clothing", "cosmetics")
- `keywords`: Optional comma-separated keyword list
- `count`: Optional number of titles to generate (default: 5)

## Title Template Types

- Review style: "{product} review | Is {keyword} really good?"
- Recommendation style: "{product} recommendation | {keyword} lovers must buy!"
- Warning style: "{product} buying guide | Don't buy {keyword}!"
- Sharing style: "{product} great finds | {keyword} amazed me"
- Unboxing style: "{product} unboxing | Is {keyword} worth it?"

## Notes

- Titles are based on popular templates; adjust keywords based on actual performance
- Choose appropriate title styles based on product characteristics and target audience
- Generate multiple times to select the best titles