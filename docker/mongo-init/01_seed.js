const dbName = "python_master";
const database = db.getSiblingDB(dbName);

database.users.deleteMany({});
database.municipalities.deleteMany({});
database.groups.deleteMany({});
database.subscriptions.deleteMany({});
database.orders.deleteMany({});
database.logs.deleteMany({});
database.reviews.deleteMany({});
database.documents.deleteMany({});
database.ai_evaluations.deleteMany({});
database.products.deleteMany({});
database.support_tickets.deleteMany({});
database.model_deployments.deleteMany({});
database.rag_chunks.deleteMany({});
database.batch_jobs.deleteMany({});

database.users.insertMany([
  {
    user_id: "u1",
    name: "Aki",
    email: "aki@example.com",
    role: "admin",
    municipality_id: "m-131016",
    group_ids: ["g-admin", "g-tokyo"],
    score: 92,
    active: true,
    created_at: ISODate("2026-01-10T09:00:00Z")
  },
  {
    user_id: "u2",
    name: "Ren",
    email: "ren@example.com",
    role: "member",
    municipality_id: "m-131016",
    group_ids: ["g-reviewer", "g-tokyo"],
    score: 75,
    active: true,
    created_at: ISODate("2026-02-15T10:30:00Z")
  },
  {
    user_id: "u3",
    name: "Mio",
    email: "mio@example.com",
    role: "member",
    municipality_id: "m-271004",
    group_ids: ["g-reviewer", "g-osaka"],
    score: 88,
    active: true,
    created_at: ISODate("2026-03-20T12:00:00Z")
  },
  {
    user_id: "u4",
    name: "Sora",
    email: "sora@example.com",
    role: "viewer",
    municipality_id: "m-141003",
    group_ids: ["g-viewer"],
    score: 61,
    active: false,
    created_at: ISODate("2026-04-01T08:15:00Z")
  }
]);

database.municipalities.insertMany([
  {
    municipality_id: "m-131016",
    code: "131016",
    name: "Chiyoda City",
    prefecture: "Tokyo",
    population: 68000,
    active: true
  },
  {
    municipality_id: "m-271004",
    code: "271004",
    name: "Osaka City",
    prefecture: "Osaka",
    population: 2750000,
    active: true
  },
  {
    municipality_id: "m-141003",
    code: "141003",
    name: "Yokohama City",
    prefecture: "Kanagawa",
    population: 3770000,
    active: true
  }
]);

database.groups.insertMany([
  {
    group_id: "g-admin",
    municipality_id: "m-131016",
    name: "Admin Operators",
    permissions: ["users:read", "users:write", "billing:read"],
    active: true
  },
  {
    group_id: "g-reviewer",
    municipality_id: "m-131016",
    name: "AI Review Team",
    permissions: ["reviews:read", "reviews:write"],
    active: true
  },
  {
    group_id: "g-tokyo",
    municipality_id: "m-131016",
    name: "Tokyo Users",
    permissions: ["dashboard:read"],
    active: true
  },
  {
    group_id: "g-osaka",
    municipality_id: "m-271004",
    name: "Osaka Users",
    permissions: ["dashboard:read"],
    active: true
  },
  {
    group_id: "g-viewer",
    municipality_id: "m-141003",
    name: "View Only",
    permissions: ["dashboard:read"],
    active: true
  }
]);

database.subscriptions.insertMany([
  {
    subscription_id: "sub-001",
    municipality_id: "m-131016",
    plan: "enterprise",
    status: "active",
    seats: 50,
    monthly_fee: 120000,
    started_at: ISODate("2026-01-01T00:00:00Z"),
    expires_at: ISODate("2026-12-31T23:59:59Z")
  },
  {
    subscription_id: "sub-002",
    municipality_id: "m-271004",
    plan: "standard",
    status: "trial",
    seats: 20,
    monthly_fee: 40000,
    started_at: ISODate("2026-05-01T00:00:00Z"),
    expires_at: ISODate("2026-07-31T23:59:59Z")
  },
  {
    subscription_id: "sub-003",
    municipality_id: "m-141003",
    plan: "standard",
    status: "past_due",
    seats: 10,
    monthly_fee: 40000,
    started_at: ISODate("2026-02-01T00:00:00Z"),
    expires_at: ISODate("2026-06-30T23:59:59Z")
  }
]);

database.orders.insertMany([
  {
    order_id: "o1",
    user_id: "u1",
    amount: 1200,
    status: "paid",
    items: [{ name: "Python Book", price: 1200, quantity: 1 }],
    created_at: ISODate("2026-05-01T10:00:00Z")
  },
  {
    order_id: "o2",
    user_id: "u2",
    amount: 800,
    status: "paid",
    items: [{ name: "Notebook", price: 400, quantity: 2 }],
    created_at: ISODate("2026-05-02T11:00:00Z")
  },
  {
    order_id: "o3",
    user_id: "u2",
    amount: 300,
    status: "cancelled",
    items: [{ name: "Pen", price: 100, quantity: 3 }],
    created_at: ISODate("2026-05-03T12:00:00Z")
  },
  {
    order_id: "o4",
    user_id: "u3",
    amount: 1500,
    status: "paid",
    items: [{ name: "MongoDB Guide", price: 1500, quantity: 1 }],
    created_at: ISODate("2026-05-04T13:00:00Z")
  },
  {
    order_id: "o5",
    user_id: "u4",
    amount: 500,
    status: "pending",
    items: [{ name: "Sticker", price: 250, quantity: 2 }],
    created_at: ISODate("2026-05-05T14:00:00Z")
  }
]);

database.logs.insertMany([
  {
    request_id: "req-001",
    action: "create_review",
    status: "ok",
    elapsed_ms: 120,
    model_name: "gpt-4.1-mini",
    created_at: ISODate("2026-06-01T09:00:00Z")
  },
  {
    request_id: "req-002",
    action: "create_review",
    status: "error",
    elapsed_ms: 450,
    model_name: "gpt-4.1-mini",
    error_code: "ai_timeout",
    created_at: ISODate("2026-06-01T09:05:00Z")
  },
  {
    request_id: "req-003",
    action: "chat",
    status: "ok",
    elapsed_ms: 90,
    model_name: "gemini-2.5-flash",
    created_at: ISODate("2026-06-01T09:10:00Z")
  }
]);

database.reviews.insertMany([
  {
    review_id: "r1",
    user_id: "u1",
    code: "def add(a, b): return a + b",
    focus: "bug",
    summary: "問題は少ないがテストを追加したい",
    suggestions: ["境界値テストを追加する", "型ヒントを付ける"],
    model_name: "gpt-4.1-mini",
    created_at: ISODate("2026-06-02T10:00:00Z")
  },
  {
    review_id: "r2",
    user_id: "u2",
    code: "db.users.deleteMany({})",
    focus: "security",
    summary: "削除条件が広すぎる",
    suggestions: ["実行前に countDocuments で確認する", "本番では dry-run を用意する"],
    model_name: "gemini-2.5-flash",
    created_at: ISODate("2026-06-02T11:00:00Z")
  }
]);

database.documents.insertMany([
  {
    doc_id: "d1",
    source: "python.md",
    title: "Python Basics",
    text: "Python functions receive input and return output. Tests protect behavior.",
    tags: ["python", "basics"]
  },
  {
    doc_id: "d2",
    source: "fastapi.md",
    title: "FastAPI Layers",
    text: "FastAPI applications often separate schema, router, service, and repository.",
    tags: ["fastapi", "api"]
  },
  {
    doc_id: "d3",
    source: "rag.md",
    title: "RAG Retrieval",
    text: "RAG quality depends on chunking, retrieval, context, citations, and evaluation.",
    tags: ["rag", "ai"]
  }
]);

database.ai_evaluations.insertMany([
  {
    eval_id: "e1",
    prompt_version: "review:v1",
    model_name: "gpt-4.1-mini",
    expected: "bug",
    actual: "bug",
    passed: true,
    reason: "",
    created_at: ISODate("2026-06-03T10:00:00Z")
  },
  {
    eval_id: "e2",
    prompt_version: "review:v1",
    model_name: "gpt-4.1-mini",
    expected: "security",
    actual: "bug",
    passed: false,
    reason: "missed security issue",
    created_at: ISODate("2026-06-03T10:05:00Z")
  },
  {
    eval_id: "e3",
    prompt_version: "review:v2",
    model_name: "gemini-2.5-flash",
    expected: "security",
    actual: "security",
    passed: true,
    reason: "",
    created_at: ISODate("2026-06-03T10:10:00Z")
  }
]);

database.products.insertMany([
  {
    product_id: "p1",
    name: "Python Book",
    category: "book",
    price: 1200,
    stock: 12,
    active: true
  },
  {
    product_id: "p2",
    name: "MongoDB Guide",
    category: "book",
    price: 1500,
    stock: 8,
    active: true
  },
  {
    product_id: "p3",
    name: "Notebook",
    category: "stationery",
    price: 400,
    stock: 30,
    active: true
  },
  {
    product_id: "p4",
    name: "Old Sticker",
    category: "goods",
    price: 250,
    stock: 0,
    active: false
  }
]);

database.support_tickets.insertMany([
  {
    ticket_id: "t1",
    user_id: "u2",
    priority: "high",
    status: "open",
    category: "billing",
    message: "Paid order is not shown on my account.",
    created_at: ISODate("2026-06-04T09:00:00Z")
  },
  {
    ticket_id: "t2",
    user_id: "u3",
    priority: "middle",
    status: "closed",
    category: "api",
    message: "FastAPI endpoint returned 422 due to invalid schema.",
    created_at: ISODate("2026-06-04T10:00:00Z")
  },
  {
    ticket_id: "t3",
    user_id: "u4",
    priority: "low",
    status: "open",
    category: "account",
    message: "I want to reactivate my account.",
    created_at: ISODate("2026-06-04T11:00:00Z")
  }
]);

database.model_deployments.insertMany([
  {
    deployment_name: "review-fast",
    model_name: "gpt-4.1-mini",
    provider: "openai",
    purpose: "code_review",
    active: true
  },
  {
    deployment_name: "chat-fast",
    model_name: "gemini-2.5-flash",
    provider: "google",
    purpose: "chat",
    active: true
  },
  {
    deployment_name: "embed-default",
    model_name: "text-embedding-3-small",
    provider: "openai",
    purpose: "embedding",
    active: true
  }
]);

database.rag_chunks.insertMany([
  {
    chunk_id: "c1",
    doc_id: "d1",
    chunk_index: 0,
    content: "Function names should describe behavior. Tests should cover normal and edge cases.",
    keywords: ["python", "function", "test"],
    embedding_model: "text-embedding-3-small"
  },
  {
    chunk_id: "c2",
    doc_id: "d2",
    chunk_index: 0,
    content: "Routers receive HTTP requests, services hold business logic, repositories access DB.",
    keywords: ["fastapi", "router", "service", "repository"],
    embedding_model: "text-embedding-3-small"
  },
  {
    chunk_id: "c3",
    doc_id: "d3",
    chunk_index: 0,
    content: "RAG should log query, retrieved chunks, model name, answer, and evaluation result.",
    keywords: ["rag", "logging", "evaluation"],
    embedding_model: "text-embedding-3-small"
  }
]);

database.batch_jobs.insertMany([
  {
    job_id: "b1",
    input_path: "data/input/reviews.jsonl",
    output_path: "data/output/reviews_result.jsonl",
    status: "done",
    total_count: 100,
    success_count: 97,
    error_count: 3,
    model_name: "gpt-4.1-mini",
    created_at: ISODate("2026-06-05T09:00:00Z")
  },
  {
    job_id: "b2",
    input_path: "data/input/tickets.jsonl",
    output_path: "data/output/tickets_result.jsonl",
    status: "running",
    total_count: 50,
    success_count: 20,
    error_count: 1,
    model_name: "gemini-2.5-flash",
    created_at: ISODate("2026-06-05T10:00:00Z")
  }
]);

database.users.createIndex({ user_id: 1 }, { unique: true });
database.users.createIndex({ role: 1, score: -1 });
database.users.createIndex({ municipality_id: 1, active: 1 });
database.users.createIndex({ group_ids: 1 });
database.municipalities.createIndex({ municipality_id: 1 }, { unique: true });
database.municipalities.createIndex({ code: 1 }, { unique: true });
database.groups.createIndex({ group_id: 1 }, { unique: true });
database.groups.createIndex({ municipality_id: 1, active: 1 });
database.subscriptions.createIndex({ subscription_id: 1 }, { unique: true });
database.subscriptions.createIndex({ municipality_id: 1, status: 1 });
database.orders.createIndex({ user_id: 1, status: 1 });
database.logs.createIndex({ action: 1, status: 1, created_at: -1 });
database.reviews.createIndex({ user_id: 1, created_at: -1 });
database.documents.createIndex({ tags: 1 });
database.ai_evaluations.createIndex({ prompt_version: 1, model_name: 1, passed: 1 });
database.products.createIndex({ category: 1, active: 1 });
database.support_tickets.createIndex({ status: 1, priority: 1, created_at: -1 });
database.model_deployments.createIndex({ deployment_name: 1 }, { unique: true });
database.rag_chunks.createIndex({ keywords: 1 });
database.batch_jobs.createIndex({ status: 1, created_at: -1 });

print(`Seeded ${dbName}`);
