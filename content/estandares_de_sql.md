title: Estándares de SQL
description: En este artículo, traducido de la wiki oficial de AzerothCore, trataremos de abarcar, temas relacionados a las buenas prácticas del lenguaje SQL. Con ejemplos sobre las tablas del emulador, pero que pueden ser modificadas, para utilizarlas en otras tablas.
date: 2021.06.07
authors: Pagani Walter
summary: En este artículo, traducido de la wiki oficial de AzerothCore, trataremos de abarcar, temas relacionados a las buenas prácticas del lenguaje SQL. Con ejemplos sobre las tablas del emulador, pero que pueden ser modificadas, para utilizarlas en otras tablas.
category: base de datos
tags: basededatos, azerothcore, sql, SQLStandards

[Documentación oficial de la wiki de AzerothCore](https://www.azerothcore.org/wiki/sql-standards)

## Consultas

### Normas generales

Para los ejemplos, utilizamos la tabla `creature_loot_template`

Siempre utilizamos **comillas simples ('')** alrededor de los valores de las cadenas, pero NUNCA alrededor de un número entero.

### INSERTAR Y ELIMINAR

Siempre se hace un DELETE antes de un INSERT para asegurar que siempre se pongan los campos en la consulta y que no se produzcan errores.

No es correcto:

```sql
INSERT INTO `creature_loot_template` (3, 884, 0, 40, 1, 1, 0, 1, 1, 'Comment');
```

Correcto:

```sql
DELETE FROM `creature_loot_template` WHERE `entry`=3 AND `item`=884;
INSERT INTO `creature_loot_template` (`Entry`, `Item`, `Reference`, `Chance`, `QuestRequired`, `LootMode`, `GroupId`, `MinCount`, `MaxCount`, `Comment`) VALUES 
(3, 884, 0, 40, 1, 1, 0, 1, 1, 'Comment');
```

### ACTUALIZACIÓN

Asegúrese de que sus consultas son precisas para evitar cambiar algo que no desea editar.

**Regla de oro**: incluya siempre todas las claves primarias en su cláusula `WHERE`.

No es correcto:

```sql
UPDATE `creature_loot_template` SET `Chance`=100 WHERE `item`=884;
```

Correcto:

```sql
UPDATE `creature_loot_template` SET `Chance`=100 WHERE `entry`=3 AND `item`=884;
```

### Variables

Las variables pueden ser buenas cuando se cambia la misma entrada en varios lugares para evitar errores.

Antes:

```sql
UPDATE `creature_template` SET `AIName`='SmartAI' WHERE `entry`=7727;

DELETE FROM `smart_scripts` WHERE `entryorguid`=7727 AND `source_type`=0;
INSERT INTO `smart_scripts` (`entryorguid`, `source_type`, `id`, `link`, `event_type`, `event_phase_mask`, `event_chance`, `event_flags`, `event_param1`, `event_param2`, `event_param3`, `event_param4`, `event_param5`, `action_type`, `action_param1`, `action_param2`, `action_param3`, `action_param4`, `action_param5`, `action_param6`, `target_type`, `target_param1`, `target_param2`, `target_param3`, `target_param4`, `target_x`, `target_y`, `target_z`, `target_o`, `comment`) VALUES 
(7727, 0, 0, 0, 0, 0, 100, 0, 2000, 4000, 2000, 4000, 0, 11, 930, 64, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 'Grimtotem Shaman - In Combat - Cast \'Chain Lightning\''),
(7727, 0, 1, 0, 2, 0, 100, 1, 0, 50, 0, 0, 0, 11, 8499, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 'Grimtotem Shaman - Between 0-50% Health - Cast \'Fire Nova\' (No Repeat)'),
(7727, 0, 2, 0, 2, 0, 100, 0, 0, 30, 0, 0, 0, 11, 8005, 64, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Grimtotem Shaman - Between 0-30% Health - Cast \'Healing Wave\'');
```

Después:

```sql
-- Grimtotem Shaman SAI
SET @ENTRY := 7727;
SET @SPELL1 := 930;
SET @SPELL2 := 8499;
SET @SPELL3 := 8005;

UPDATE `creature_template` SET `AIName` = 'SmartAI' WHERE `entry` = @ENTRY;

DELETE FROM `smart_scripts` WHERE `entryorguid` = @ENTRY AND `source_type` = 0;
INSERT INTO `smart_scripts` (`entryorguid`, `source_type`, `id`, `link`, `event_type`, `event_phase_mask`, `event_chance`, `event_flags`, `event_param1`, `event_param2`, `event_param3`, `event_param4`, `event_param5`, `action_type`, `action_param1`, `action_param2`, `action_param3`, `action_param4`, `action_param5`, `action_param6`, `target_type`, `target_param1`, `target_param2`, `target_param3`, `target_param4`, `target_x`, `target_y`, `target_z`, `target_o`, `comment`) VALUES 
(@ENTRY, 0, 0, 0, 0, 0, 100, 0, 2000, 4000, 2000, 4000, 0, 11, @SPELL1, 64, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 'Grimtotem Shaman - In Combat - Cast \'Chain Lightning\''),
(@ENTRY, 0, 1, 0, 2, 0, 100, 1, 0, 50, 0, 0, 0, 11, @SPELL2, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 'Grimtotem Shaman - Between 0-50% Health - Cast \'Fire Nova\' (No Repeat)'),
(@ENTRY, 0, 2, 0, 2, 0, 100, 0, 0, 30, 0, 0, 0, 11, @SPELL3, 64, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Grimtotem Shaman - Between 0-30% Health - Cast \'Healing Wave\'');
```


### Consultas cortas

Siempre mantenemos el código lo más corto posible para limitar el tamaño de los archivos y disminuir el número de consultas necesarias para su ejecución.

No es correcto:

```sql
DELETE FROM `table_1` WHERE `entry` = 1000;
DELETE FROM `table_1` WHERE `entry` = 2000;
DELETE FROM `table_1` WHERE `entry` = 3000;

INSERT INTO `table_1` VALUES (1000, ...);
INSERT INTO `table_1` VALUES (2000, ...);
INSERT INTO `table_1` VALUES (3000, ...);

UPDATE `table_1` SET `field_1` = 'someValue' WHERE `entry` = 1000;
UPDATE `table_1` SET `field_1` = 'someValue' WHERE `entry` = 2000;
UPDATE `table_1` SET `field_1` = 'someValue' WHERE `entry` = 3000;
```

Correcto:

```sql
DELETE FROM `table_1` WHERE `entry` IN (1000, 2000, 3000);

INSERT INTO `table_1` VALUES
(1000, ...),
(2000, ...),
(3000, ...);

UPDATE `table_1` SET `field_1` = 'someValue' WHERE `entry` IN (1000, 2000, 3000);
```

### Banderas y Bits

Para los campos de la base de datos en los que trabajamos con banderas siempre es preferible que añadamos o eliminemos banderas en lugar de sobrescribirlas.

No es correcto:

```sql
UPDATE `creature_template` SET `mechanic_immune_mask` = 617299803 WHERE `entry` = 7727;
```

Correcto:

```sql
-- Añadir banderas
UPDATE `creature_template` SET `mechanic_immune_mask`=`mechanic_immune_mask`|64|256|1024 WHERE `entry` = 7727;

-- Eliminación de banderas
UPDATE `creature_template` SET `mechanic_immune_mask`=`mechanic_immune_mask`&~(64|256|1024) WHERE `entry` = 7727;
```

## Tablas y columnas

### Números enteros

No definimos el ancho de un entero cuando creamos nuevas columnas. (El ancho está obsoleto en versiones posteriores de MySQL 8)

```sql
TINYINT(M)   -> TINYINT
SMALLINT(M)  -> SMALLINT
INT(M)       -> INT
MEDIUMINT(M) -> MEDIUMINT
BIGINT(M)    -> BIGINT

BOOL         -> Nunca se utiliza, sinónimo de TINYINT. 0 = false <> 0 = true
```

### Flotante, Doble, Decimal

Estos tipos de datos no pueden ser UNSIGNED y por lo tanto utilizamos CHECK CONSTRAINTS en su lugar. (UNSIGNED Float, Double, Decimal está obsoleto en versiones posteriores de MySQL 8)

```
FLOAT UNSIGNED -> CHECK (`column`>=0)
```

### Codificación de caracteres

Usamos UTF8MB4 donde antes se usaba UTF8 o UTF8MB3. (utf8 es un alias y utf8mb3 está obsoleto en versiones posteriores de MySQL 8)

```sql
utf8    -> utf8mb4
utf8mb3 -> utf8mb4

Esto también se aplica a `utf8_unicode_ci`, etc.
```

### Comprobar restricciones

Puede ver [aquí](https://github.com/Azerothcore/azerothcore-wotlk/blob/master/data/sql/base/db_auth/realmlist.sql) cómo se realizan los controles.

Todas las restricciones de verificación activas se pueden encontrar utilizando esta consulta:

```sql
SELECT * FROM `information_schema`.CHECK_CONSTRAINTS;
```

## Nota para el encargado de revisar el SQL

Cuando trabajemos con GUID's, asegurémonos de utilizar el menor número de entradas posible para rellenar los huecos en la base de datos. Esto puede hacerse fácilmente con herramientas como [Unused GUID Searcher](https://github.com/azerothcore/unused-guid-search).
También puedes leer este otro documento: [Cómo obtener registros libres en una tabla](https://pangolp.github.io/como-obtener-registros-libres-en-una-tabla.html)
