queries = {
    "column": {
        "head": "select {column} from {table} limit {n};",
        "all": "select {column} from {table};",
        "unique": "select distinct {column} from {table};",
        "sample": "select {column} from {table} order by random() limit {n};"
    },
    "table": {
        "select": "select {columns} from {table};",
        "head": "select * from {table} limit {n};",
        "all": "select * from {table};",
        "unique": "select distinct {columns} from {table};",
        "sample": "select * from {table} order by random() limit {n};"
    },
    "system": {
        "schema_no_system": """
            select
                table_name
                , column_name
                , data_type
            from
                information_schema.columns
            where
                table_schema not in ('information_schema');
            """,
        "schema_with_system": """
            select
                table_name
                , column_name
                , data_type
            from
                information_schema.columns;
            """,
        "schema_specified": """
            select
                table_schema
                , table_name
                , column_name
                , data_type
            from
                information_schema.columns
            where table_schema in (%s);
            """
    }
}
