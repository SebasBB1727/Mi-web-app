from supabase import create_client

def inicializar_db():
    client = create_client("https://wkcpobfnenbjmzzwptyd.supabase.co","SupabaseHybridge2028")
    return client
