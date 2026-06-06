from app.models import Record


def default_records() -> list[Record]:
    return [
        Record("r1", "Pet Adoption Desk 首轮安排", "nina", "进行中", "高", "先确认核心节点和资源。"),
        Record("r2", "Pet Adoption Desk 周会", "mira", "待处理", "中", "整理当前风险和后续动作。"),
    ]
