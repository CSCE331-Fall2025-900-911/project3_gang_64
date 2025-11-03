set dotenv-load
set dotenv-required
set export


dev: 
    pnpm run dev

deploy: 
    pnpm run deploy

repl +ARGS='':
    psql -d gang_64_db {{ARGS}}

reset-db:
    just repl -f seeding/reset.sql
    pnpm drizzle-kit push 
    just repl -f seeding/load.sql