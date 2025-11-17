set dotenv-load
set dotenv-required
set export


dev: 
    pnpm run dev

deploy: 
    pnpm run deploy

repl +ARGS='':
    psql -d gang_64_db {{ARGS}}

translate LCL:
    pnpm dlx @inlang/cli machine translate --project ./project.inlang --locale "en" --targetLocales "{{LCL}}"

reset-db:
    just repl -f seeding/reset.sql
    pnpm drizzle-kit push 
    just repl -f seeding/load.sql