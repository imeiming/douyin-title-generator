# Douyin Title Generator Skill

This skill integrates with the existing `douyin-profit-calculator` skill ecosystem to provide comprehensive Douyin content creation support.

## Integration Points

### Shared Data Directory
Both skills use the same workspace structure and can share data through the common examples directory structure.

### Cross-Skill Triggers
- When `douyin-profit-calculator` identifies high-profit products, users can immediately request title generation for those products
- The title generator can suggest titles optimized for the product categories identified by the profit calculator

### Usage Workflow
1. User provides sales data → `douyin-profit-calculator` analyzes profit margins
2. User requests titles for high-margin products → `douyin-title-generator` creates targeted viral titles
3. Both skills maintain separate but compatible data structures in their respective `examples/` directories

## Dependencies
- Python 3.6+
- Optional: jieba (for better Chinese text segmentation)

## File Structure
```
douyin-title-generator/
├── SKILL.md                 # Skill description and usage instructions
├── _meta.json              # Metadata and trigger configuration
├── README.md               # Integration documentation
├── examples/               # Title libraries (JSON files by category)
│   ├── general.json        # Default title examples
│   └── example_usage.md    # Usage examples
└── scripts/
    └── title_generator.py  # Core title analysis and generation logic
```

## Auto-Trigger Keywords
The skill automatically activates when user messages contain:
- "标题"
- "爆款" 
- "抖音标题"
- "短视频标题"
- "热门标题"
- "标题生成"
- "标题建议"

## Development Notes
- The skill is designed to be extensible for different content categories
- Title patterns are learned from user-provided examples
- Generated titles follow proven viral content formulas
- Integration with profit calculator enables data-driven title optimization