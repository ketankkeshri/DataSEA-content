# Replication Basics

Replication is a crucial component in PostgreSQL architecture, enabling high availability and data redundancy. Understanding how replication works equips Data Engineers with the skills to implement robust data solutions that ensure minimal downtime and data loss.

## What is Replication?

Replication in PostgreSQL involves duplicating data from one database server (the primary) to one or more servers (the replicas). This process ensures that data remains accessible even if the primary server fails. The two main types of replication in PostgreSQL are:

- **Streaming Replication:** This method continuously sends changes from the primary to the replicas in real-time.
- **Logical Replication:** This allows for selective replication of data, letting you replicate specific tables or databases instead of the entire cluster.

### Streaming Replication Setup

To set up streaming replication, you need to configure both the primary and the replica servers. Here's a quick setup guide:

1. **On the Primary Server:**
   - Modify `postgresql.conf` to enable replication:
     ```sql
     # postgresql.conf
     wal_level = replica
     max_wal_senders = 3
     wal_keep_segments = 64
     ```
   - Allow the replica to connect in `pg_hba.conf`:
     ```plaintext
     # pg_hba.conf
     host    replication     all             {REPLICA_IP}/32          md5
     ```

2. **On the Replica Server:**
   - Create a base backup using `pg_basebackup`:
     ```bash
     pg_basebackup -h {PRIMARY_IP} -D /var/lib/postgresql/data -U {REPLICA_USER} -P --wal-method=stream
     ```
   - Set up the `recovery.conf` file:
     ```plaintext
     # recovery.conf
     standby_mode = 'on'
     primary_conninfo = 'host={PRIMARY_IP} port=5432 user={REPLICA_USER} password={REPLICA_PASSWORD}'
     trigger_file = '/tmp/postgresql.trigger'
     ```

3. **Start the Replica:**
   - Simply start the PostgreSQL service on the replica:
     ```bash
     sudo systemctl start postgresql
     ```

## Monitoring Replication

After setting up replication, monitoring its health is vital. You can use SQL commands to check the status:

```sql
SELECT
    pid,
    usename,
    application_name,
    client_addr,
    state,
    sync_state
FROM pg_stat_replication;
```

This query will provide useful information about connected replicas, their states, and any potential issues.

### Troubleshooting Common Issues

When working with replication, you may encounter some common issues:

- **Replication Lag:** This occurs when the replica falls behind the primary server. Ensure that the network bandwidth is sufficient and that the replica is not overloaded with queries.
- **Connection Issues:** If replicas fail to connect to the primary, double-check network settings and the `pg_hba.conf` configuration.

## Common pitfalls

- **Ignoring WAL Size:** Not monitoring the Write Ahead Log (WAL) size can lead to disk space issues on the primary server.
- **Neglecting Failover Procedures:** Failing to implement automated failover can result in prolonged downtime during primary server failures.
- **Unconfigured Replication Slots:** If using logical replication, ensure that replication slots are correctly configured to avoid data loss.

## In a nutshell

- Replication is essential for data redundancy and high availability.
- Streaming and logical replication are the two main types in PostgreSQL.
- Proper setup includes configuring both primary and replica servers.
- Monitoring replication health is crucial for performance and reliability.
- Be cautious of common pitfalls like WAL size and failover procedures.