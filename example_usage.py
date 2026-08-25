from client import NaturalLanguageFullstackWebPrototypeCompilerClient

def main():
    client = NaturalLanguageFullstackWebPrototypeCompilerClient()
    res = client.compile_fullstack_web_app('Fullstack analytics dashboard with Stripe webhooks and PostgreSQL')
    print('Build ID: ' + res['prototype_build_id'] + ' (' + str(res['components_generated_count']) + ' components in ' + str(res['build_time_seconds']) + 's)')
    print('Live Preview: ' + res['live_preview_url'])
    print('DB Migrated: ' + str(res['database_schema_sql_migrated']) + ' | GitHub Synced: ' + str(res['github_repository_synced']))

if __name__ == '__main__':
    main()
